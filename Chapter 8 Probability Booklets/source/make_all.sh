#!/bin/bash
# Build, render, check layout and shrink all five booklets.
set -e
cd "$(dirname "$0")"
mkdir -p out final
ln -sfn "$PWD/fonts" out/fonts; ln -sfn "$PWD/img" out/img
for v in std_student std_teacher ext_student ext_teacher; do python3 build.py $v; done
for f in out/*.html; do
  n=$(basename "${f%.html}")
  node render.js "$f" "out/$n.raw.pdf" | grep -v '^wrote' || true
  python3 shrink.py "out/$n.raw.pdf" "final/$n.pdf"
done
ls -la final
