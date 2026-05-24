-- ============================================================
--  Sistema de Biblioteca — Datos de Prueba
-- ============================================================

-- USERS
INSERT INTO users (id, username, email, password, role) VALUES
  ('11111111-0000-0000-0000-000000000001', 'admin',      'admin@biblioteca.pe',    'hashed_pass_1', 'admin'),
  ('11111111-0000-0000-0000-000000000002', 'librarian1', 'lib1@biblioteca.pe',     'hashed_pass_2', 'librarian');

-- CATEGORIES
INSERT INTO categories (id, name, description, created_id, modified_id) VALUES
  ('22222222-0000-0000-0000-000000000001', 'Fiction',          'Narrative literature works',           '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001'),
  ('22222222-0000-0000-0000-000000000002', 'Science',          'Scientific and technical books',       '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001'),
  ('22222222-0000-0000-0000-000000000003', 'History',          'Historical and social science books',  '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001'),
  ('22222222-0000-0000-0000-000000000004', 'Technology',       'Programming and software engineering', '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001');

-- AUTHORS
INSERT INTO authors (id, names, fatherSurname, motherSurname, nationality, created_id, modified_id) VALUES
  ('33333333-0000-0000-0000-000000000001', 'Gabriel',  'García',   'Márquez', 'Colombian', '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001'),
  ('33333333-0000-0000-0000-000000000002', 'George',   'Orwell',   NULL,      'British',   '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001'),
  ('33333333-0000-0000-0000-000000000003', 'Robert C.','Martin',   NULL,      'American',  '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001'),
  ('33333333-0000-0000-0000-000000000004', 'Yuval',    'Harari',   'Noah',    'Israeli',   '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001');

-- BOOKS
INSERT INTO books (id, title, isbn, stock, editorial, publicationYear, category_id, created_id, modified_id) VALUES
  ('44444444-0000-0000-0000-000000000001', 'One Hundred Years of Solitude', '978-0-06-088328-7', 3, 'Harper & Row',    1967, '22222222-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001'),
  ('44444444-0000-0000-0000-000000000002', '1984',                          '978-0-45-228285-3', 5, 'Secker & Warburg',1949, '22222222-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001'),
  ('44444444-0000-0000-0000-000000000003', 'Clean Code',                    '978-0-13-235088-4', 4, 'Prentice Hall',   2008, '22222222-0000-0000-0000-000000000004', '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001'),
  ('44444444-0000-0000-0000-000000000004', 'Sapiens',                       '978-0-06-231609-7', 6, 'Harper Collins',  2011, '22222222-0000-0000-0000-000000000003', '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001');

-- AUTHORS_BOOKS  (relación N:M)
INSERT INTO authors_books (author_id, book_id, created_id, modified_id) VALUES
  ('33333333-0000-0000-0000-000000000001', '44444444-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001'),
  ('33333333-0000-0000-0000-000000000002', '44444444-0000-0000-0000-000000000002', '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001'),
  ('33333333-0000-0000-0000-000000000003', '44444444-0000-0000-0000-000000000003', '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001'),
  ('33333333-0000-0000-0000-000000000004', '44444444-0000-0000-0000-000000000004', '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001');

-- MEMBERS
INSERT INTO members (id, names, fatherSurname, motherSurname, email, phone, address, user_id, created_id, modified_id) VALUES
  ('55555555-0000-0000-0000-000000000001', 'María',  'López',   'Torres',  'maria.lopez@mail.com',  '959000001', 'Av. Lima 123, Arequipa',  NULL, '11111111-0000-0000-0000-000000000002', '11111111-0000-0000-0000-000000000002'),
  ('55555555-0000-0000-0000-000000000002', 'Carlos', 'Mamani',  'Quispe',  'carlos.mamani@mail.com','959000002', 'Jr. Cusco 456, Arequipa',  NULL, '11111111-0000-0000-0000-000000000002', '11111111-0000-0000-0000-000000000002');

-- LOANS
INSERT INTO loans (member_id, book_id, loanDate, dueDate, returnDate, created_id, modified_id) VALUES
  ('55555555-0000-0000-0000-000000000001', '44444444-0000-0000-0000-000000000001', '2025-05-01', '2025-05-15', '2025-05-14', '11111111-0000-0000-0000-000000000002', '11111111-0000-0000-0000-000000000002'),
  ('55555555-0000-0000-0000-000000000002', '44444444-0000-0000-0000-000000000003', '2025-05-10', '2025-05-24', NULL,         '11111111-0000-0000-0000-000000000002', '11111111-0000-0000-0000-000000000002');

-- ============================================================
-- CONSULTAS DE VERIFICACIÓN
-- ============================================================

-- Ver todos los libros con su categoría
SELECT b.title, b.isbn, b.stock, c.name AS category
FROM books b
JOIN categories c ON b.category_id = c.id
WHERE b.status = 1;

-- Ver libros con sus autores
SELECT b.title, CONCAT(a.names, ' ', a.fatherSurname) AS author
FROM books b
JOIN authors_books ab ON b.id = ab.book_id
JOIN authors a ON ab.author_id = a.id
WHERE b.status = 1;

-- Ver prestamos activos (sin fecha de devolucion)
SELECT
    CONCAT(m.names, ' ', m.fatherSurname) AS member,
    b.title AS book,
    l.loanDate,
    l.dueDate
FROM loans l
JOIN members m ON l.member_id = m.id
JOIN books b   ON l.book_id   = b.id
WHERE l.returnDate IS NULL
  AND l.status = 1;