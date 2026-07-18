#!/usr/bin/env node

const templates: Record<string, string> = {
  node: `node_modules/
dist/
.env
*.log
.DS_Store
coverage/
`,
  python: `__pycache__/
*.pyc
.venv/
*.egg-info/
dist/
.env
`,
  react: `node_modules/
build/
.env
*.log
.DS_Store
`,
  rust: `target/
Cargo.lock
**/*.rs.bk
`
};

function main() {
  const type = (process.argv[2] || "node").replace("--type=", "").replace("--type", "");
  const content = templates[type] || templates.node;
  console.log(content);
}

main();
