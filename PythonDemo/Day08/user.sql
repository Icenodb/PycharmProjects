create table user(
   uid integer primary key autoincrement not null,
	 name  text(10) not null,
   sex   text(1) not null,
   nation text(10) not null,
   currjob  text(50) not null,
   sal      real(10,2) not null,
   memo
);