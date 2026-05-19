CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255) NOT NULL,
  rating FLOAT CHECK (rating <= 10)
);

CREATE TABLE reviews (
  id SERIAL PRIMARY KEY,
  book_id INTEGER REFERENCES books(id) ON DELETE CASCADE,
  review_text TEXT NOT NULL,
  reviewer_name VARCHAR(255) NOT NULL
);