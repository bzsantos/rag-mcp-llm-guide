#!/usr/bin/env bash
# Comandos usados no Capítulo 27

cd ..
npm create vite@latest assistente-corporativo-web -- --template react
cd assistente-corporativo-web
npm install

npm run dev

mkdir -p src/services src/pages
