import React, { useState, useEffect } from 'react';


function Books()
{
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/books").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div className='row'>
      <center><h2>Books List</h2></center>
      {(typeof data.books === 'undefined') ? (
        <p>Loading...</p>
      ) : (data.books.map((book, i) => (
        <div key={i} className='column'>
            <div className="card">
              <img src={book.img} />
              <div className="container">
                <h4><b>{book.name}</b></h4>
                <p>{book.author}</p>
                <p>{book.releasedate}</p>
                <p>{book.isbn}</p>
                <i class="fa fa-trash-o"></i>
              </div>
          </div>
        </div>
      ))
      )}
    </div>

  )
}

export default Books;