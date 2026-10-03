  let n = `${lv(e.severity)}: ${e.message}`;
  return e.suggest && e.suggest.length > 0 && (n += `; SUGGESTED FIXES: ${e.suggest.map((r) => r.message).join(" OR ")}.`), n;
}
function fv(e) {
  return (e.severity ?? xe.ERROR) === xe.ERROR;
}
const pv = `This tool validates Liquid codeblocks, Liquid files, and supporting Theme files (e.g. JSON locale files, JSON config files, JSON template files, JavaScript files, CSS files, and SVG files) generated or updated by LLMs to ensure they don't have hallucinated Liquid content, invalid syntax, or incorrect references${Jt}`;
function hv() {
  return {
    name: "validate_theme",
    description: `${pv}. Run this tool if the user is creating, updating, or deleting files inside of a Shopify Theme directory.`,
