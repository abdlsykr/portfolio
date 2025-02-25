document.addEventListener('DOMContentLoaded', function () {
    const bookForm = document.getElementById('inputBook');
    const searchForm = document.getElementById('searchBook');
    const incompleteBookshelfList = document.getElementById('incompleteBookshelfList');
    const completeBookshelfList = document.getElementById('completeBookshelfList');
    const bookTitle = document.getElementById('inputBookTitle');
    const bookAuthor = document.getElementById('inputBookAuthor');
    const bookYear = document.getElementById('inputBookYear');
    const bookIsComplete = document.getElementById('inputBookIsComplete');
    const searchBookTitle = document.getElementById('searchBookTitle');
    let books = JSON.parse(localStorage.getItem('books')) || [];

    function renderBooks(filteredBooks = books) {
        incompleteBookshelfList.innerHTML = '';
        completeBookshelfList.innerHTML = '';
        
        filteredBooks.forEach(book => {
            const bookElement = createBookElement(book);
            if (book.isComplete) {
                completeBookshelfList.append(bookElement);
            } else {
                incompleteBookshelfList.append(bookElement);
            }
        });
    }

    function createBookElement(book) {
        const bookElement = document.createElement('article');
        bookElement.classList.add('book_item');
        bookElement.innerHTML = `
            <h3>${book.title}</h3>
            <p>Penulis: ${book.author}</p>
            <p>Tahun: ${book.year}</p>
            <div class="action">
                <button class="green" onclick="toggleBookStatus(${book.id})">${book.isComplete ? 'Belum selesai dibaca' : 'Selesai dibaca'}</button>
                <button class="red" onclick="deleteBook(${book.id})">Hapus buku</button>
            </div>
        `;
        return bookElement;
    }

    function addBook(event) {
        event.preventDefault();

        const newBook = {
            id: Date.now(),
            title: bookTitle.value,
            author: bookAuthor.value,
            year: parseInt(bookYear.value),
            isComplete: bookIsComplete.checked
        };

        books.push(newBook);
        saveBooks();
        renderBooks();
        bookForm.reset();
    }

    window.toggleBookStatus = function (id) {
        const book = books.find(book => book.id === id);
        book.isComplete = !book.isComplete;
        saveBooks();
        renderBooks();
    };

    window.deleteBook = function (id) {
        books = books.filter(book => book.id !== id);
        saveBooks();
        renderBooks();
    };

    function saveBooks() {
        localStorage.setItem('books', JSON.stringify(books));
    }

    function searchBooks(event) {
        event.preventDefault();
        const query = searchBookTitle.value.toLowerCase();
        const filteredBooks = books.filter(book => book.title.toLowerCase().includes(query));
        renderBooks(filteredBooks);
    }

    bookForm.addEventListener('submit', addBook);
    searchForm.addEventListener('submit', searchBooks);

    renderBooks();
});
