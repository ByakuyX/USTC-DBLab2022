drop database if exists db;
create database db;
use db;

# 银行
create table Bank(
   Bank_Name    varchar(50) not null primary key,
   City         varchar(50) not null,
   Assets       float(15)   not null
);

# 部门
create table Department
(
   Department_ID         varchar(50) not null primary key,
   Department_Name       varchar(50) not null,
   Department_Type       varchar(50),
   Manager_ID   		 varchar(50)
);

# 员工
create table Employee
(
   Employee_ID         varchar(50) not null primary key,
   Employee_Name       varchar(50) not null,
   Bank_Name       	   varchar(50) not null,
   Department_ID       varchar(50),
   Employee_Tel        int,
   Employee_Address    varchar(50),
   Work_Date   		   date
);
alter table Employee add constraint FK_Belong_To foreign key (Department_ID)
      references Department (Department_ID);
alter table Employee add constraint FK_Employ foreign key (Bank_Name)
      references Bank (Bank_Name);

# 客户
create table Client
(
   Client_ID       varchar(50) not null primary key,
   Client_Name     varchar(50) not null,
   Client_Tel      varchar(50),
   Client_Address  varchar(50),
   Contact_Name    varchar(50) not null,
   Contact_Email   varchar(50),
   Contact_Tel     varchar(50),
   Relation		    varchar(50)
);

# 账户
create table Account
(
   Account_ID      varchar(50) not null primary key,
   Bank_Name       varchar(50) not null,
   Balance         float(15)   not null,
   Opening_Date    date        not null
);
alter table Account add constraint FK_Open foreign key (Bank_Name)
      references Bank (Bank_Name);

# 储蓄账户
create table Saving_Account
(
   Account_ID      varchar(50) not null primary key,
   Interest_Rate   float(15),
   Currency_Type   varchar(50)
);
alter table Saving_Account add constraint FK_Account_Type1 foreign key (Account_ID)
      references Account (Account_ID);

# 支票账户
create table Checking_Account
(
   Account_ID      varchar(50) not null primary key,
   Overdraft       float(15)
);
alter table Checking_Account add constraint FK_Account_Type2 foreign key (Account_ID)
      references Account (Account_ID);

# 持有账户
create table Own
(
   Client_ID       varchar(50) not null,
   Account_ID      varchar(50) not null,
   primary key (Client_ID, Account_ID)
);
alter table Own add constraint FK_Own1 foreign key (Client_ID)
   references Client (Client_ID);
alter table Own add constraint FK_Own2 foreign key (Account_ID)
   references Account (Account_ID);
   
# 开户检查
create table Checking
(
   Client_ID       varchar(50) not null,
   Bank_Name       varchar(50) not null,
   Account_Type    int         not null,
   primary key (Client_ID, Bank_Name, Account_Type)
);
alter table Checking add constraint FK_Checking1 foreign key (Client_ID)
	references Client (Client_ID);
alter table Checking add constraint FK_Checking2 foreign key (Bank_Name)
	references Bank (Bank_Name);

# 贷款
create table Loan
(
   Loan_ID         varchar(50) not null primary key,
   Bank_Name       varchar(50) not null,
   Loan_Amount     float(15)   not null,
   Pay_already     float(15)   not null,
   Loan_Status	    varchar(50) not null
);
alter table Loan add constraint FK_Make_Loan foreign key (Bank_Name)
	references Bank (Bank_Name);
    
# 发放
create table Pay
(
   Pay_ID          varchar(50) not null primary key,
   Loan_ID         varchar(50) not null,
   Pay_Amount      float(15)   not null,
   Pay_Date        date        not null
);
alter table Pay add constraint FK_Apply foreign key (Loan_ID)
      references Loan (Loan_ID);

# 持有贷款
create table Bear
(
   Client_ID       varchar(50) not null,
   Loan_ID         varchar(50) not null,
   primary key (Client_ID, Loan_ID)
);
alter table Bear add constraint FK_Bear1 foreign key (Client_ID)
   references Client (Client_ID);
alter table Bear add constraint FK_Bear2 foreign key (Loan_ID)
   references Loan (Loan_ID);
   
# 服务
create table Service
(
   Client_ID         varchar(50) not null,
   Employee_ID       varchar(50) not null,
   Service_Type      varchar(50),
   primary key (Client_ID, Employee_ID)
);
alter table Service add constraint FK_Service foreign key (Client_ID)
      references Client (Client_ID);
alter table Service add constraint FK_Service2 foreign key (Employee_ID)
      references Employee (Employee_ID);

insert into Bank value('A', '1', '11451400');
insert into Bank value('B', '1', '19198100');
insert into Bank value('C', '2', '98765432');
insert into Bank value('D', '3', '23333333');
insert into Bank value('T''H', 'LTS', '114');
insert into Department value('1', 'X', '1', '1');
insert into Department value('2', 'Y', '2', '2');
insert into Employee value('1', 'A', 'A', '1', '1', '1', '2020-01-01');
insert into Employee value('2', 'B', 'C', '2', '1', '1', '2020-01-01');
	 