Create database library ;
use library;
create table books
			(book_code int not NULL primary key,
			book_name varchar(50),
			price int(3),
			status varchar(2)); 
            
Create table borrower_details 
				(code int ,
                name varchar(60),
                address varchar(150) , 
                phone int , 
                issuedate int , 
                period int );