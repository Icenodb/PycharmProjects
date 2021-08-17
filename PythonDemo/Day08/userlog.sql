create table userlog(
   logid integer primary key autoincrement not null,
	 uid   integer not null references user(uid),
	 bdate text(10) not null,
	 edate text(10),
	 job   text(50) not null,
	 sal   real(10,2) not null
);