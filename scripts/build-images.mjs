import fg from "fast-glob";
import fse from "fs-extra";
import path from "path";
import sharp from "sharp";
import chokidar from "chokidar";

const SRC = "assets/img_src";
const OUT = "assets/img";

// choose widths you want generated
const WIDTHS = [360, 480, 640, 768, 960, 1100, 1600];

// map *output* file extensions to Sharp's internal format name
const FORMATS = [
  { ext: "avif", format: "avif", opts: { quality: 55 } },
  { ext: "webp", format: "webp", opts: { quality: 70 } },
  { ext: "jpg",  format: "jpeg", opts: { quality: 78, progressive: true } },
];

async function processOne(file) {
  const rel  = path.relative(SRC, file);     // e.g. "news/ap-highlight.jpg"
  const dir  = path.dirname(rel);            // "news"
  const base = path.parse(rel).name;         // "ap-highlight"
  await fse.ensureDir(path.join(OUT, dir));

  // generate each size/format (sequential to avoid too many open files)
  for (const w of WIDTHS) {
    for (const fmt of FORMATS) {
      const out = path.join(OUT, dir, `${base}-${w}.${fmt.ext}`);
      await sharp(file)                        // fresh instance each time
        .rotate()                              // respect EXIF orientation
        .resize({ width: w, withoutEnlargement: true })
        .toFormat(fmt.format, fmt.opts)        // <-- the important change
        .toFile(out);
      console.log("✔", path.join(dir, `${base}-${w}.${fmt.ext}`));
    }
  }
}

async function buildAll() {
  const files = await fg(`${SRC}/**/*.{jpg,jpeg,png,webp}`, {
    caseSensitiveMatch: false,
  });
  for (const file of files) await processOne(file);
}

// run once
buildAll().catch(err => { console.error(err); process.exit(1); });

// optional: watch mode (npm run watch:images)
if (process.argv.includes("--watch")) {
  chokidar
    .watch(`${SRC}/**/*.{jpg,jpeg,png,webp}`, { ignoreInitial: true })
    .on("add", processOne)
    .on("change", processOne);
  console.log("Watching", SRC, "…");
}
