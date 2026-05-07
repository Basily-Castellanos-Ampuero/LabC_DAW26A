4// Dependencias: express, markdown-it, cors

const fs = require('fs');
const path = require('path');
const express = require('express');
const cors = require('cors');
const MarkdownIt = require('markdown-it');

const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true,
});

const app = express();
const PORT = 3000;

const MD_DIR = path.resolve(__dirname, 'markdown_files');

// Crear directorio si no existe
if (!fs.existsSync(MD_DIR)) {
  fs.mkdirSync(MD_DIR, { recursive: true });
}

// Middlewares
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

//  Rutas estáticas 
// Servir index.html en /lab03 y /lab03/
app.get(['/lab03', '/lab03/'], (req, res) => {
  res.sendFile(path.resolve(__dirname, 'index.html'));
});

// API: Listar archivos Markdown 
// GET /lab03/api/files
// Responde con JSON: { files: [ { name, size, modified }, ... ] }
app.get('/lab03/api/files', (req, res) => {
  fs.readdir(MD_DIR, (err, items) => {
    if (err) {
      console.error('Error leyendo directorio:', err);
      return res.status(500).json({ error: 'No se pudo leer el directorio de archivos.' });
    }

    const mdFiles = items.filter(f => f.endsWith('.md'));

    // Obtener metadata de cada archivo
    const files = mdFiles.map(name => {
      const stats = fs.statSync(path.join(MD_DIR, name));
      return {
        name,
        size: stats.size,
        modified: stats.mtime.toISOString(),
      };
    });

    files.sort((a, b) => new Date(b.modified) - new Date(a.modified));

    res.json({ files });
  });
});

// ─── API: Ver contenido de un archivo Markdown ───────────────────────────────
// GET /lab03/api/files/:name
// Responde con JSON: { name, raw, html }
app.get('/lab03/api/files/:name', (req, res) => {
  const fileName = req.params.name;

  // Seguridad: solo permitir nombres de archivo simples (sin path traversal)
  if (!fileName.endsWith('.md') || fileName.includes('/') || fileName.includes('..')) {
    return res.status(400).json({ error: 'Nombre de archivo inválido.' });
  }

  const filePath = path.join(MD_DIR, fileName);

  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      if (err.code === 'ENOENT') {
        return res.status(404).json({ error: 'Archivo no encontrado.' });
      }
      console.error('Error leyendo archivo:', err);
      return res.status(500).json({ error: 'No se pudo leer el archivo.' });
    }

    const htmlContent = md.render(data);

    res.json({
      name: fileName,
      raw: data,
      html: htmlContent,
    });
  });
});

// ─── API: Crear nuevo archivo Markdown ───────────────────────────────────────
// POST /lab03/api/files
// Body JSON: { name: "titulo", content: "# Contenido..." }
// Responde con JSON: { success, name, message }
app.post('/lab03/api/files', (req, res) => {
  let { name, content } = req.body;

  if (!name || !content) {
    return res.status(400).json({ error: 'Se requieren los campos "name" y "content".' });
  }

  if (!name.endsWith('.md')) {
    name = name + '.md';
  }

  name = path.basename(name);

  if (name.includes('..') || name.includes('/')) {
    return res.status(400).json({ error: 'Nombre de archivo inválido.' });
  }

  const filePath = path.join(MD_DIR, name);

  if (fs.existsSync(filePath)) {
    return res.status(409).json({ error: `El archivo "${name}" ya existe.` });
  }

  fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) {
      console.error('Error guardando archivo:', err);
      return res.status(500).json({ error: 'No se pudo guardar el archivo.' });
    }

    console.log(`[+] Nuevo archivo creado: ${name}`);
    res.status(201).json({
      success: true,
      name,
      message: `Archivo "${name}" creado correctamente.`,
    });
  });
});

// ─── Inicio del servidor ──────────────────────────────────────────────────────
app.listen(PORT, () => {
  console.log(`\n Servidor escuchando en: http://localhost:${PORT}`);
  console.log(` Archivos Markdown en:   ${MD_DIR}`);
  console.log(` Aplicación web en:      http://localhost:${PORT}/lab03\n`);
});
