insert into Client value('ddd', 1, 1, 2, 1, 2, 3, 4);
insert into Client value('dd', 1, 1, 2, 1, 2, 3, 4);
insert into Client value('d', 1, 1, 2, 1, 2, 3, 4);
insert into Client value('fff', 1, 1, 2, 1, 2, 3, 4);
insert into Client value('ff', 1, 1, 2, 1, 2, 3, 4);
insert into Client value('f', 1, 1, 2, 1, 2, 3, 4);
insert into Client value('eee', 1, 1, 2, 1, 2, 3, 4);
insert into Client value('ee', 1, 1, 2, 1, 2, 3, 4);
insert into Client value('e', 1, 1, 2, 1, 2, 3, 4);
insert into Loan value(114514, 'A', 1919, 0, '未发放');
insert into Loan value(114515, 'D', 1920, 20, '发放中');
insert into Loan value(114516, 'A', 1919, 1919, '已发放');
insert into pay value(10, 114515, 20, '2020-09-08');
insert into pay value(11, 114516, 1910, '2021-08-09');
insert into pay value(12, 114516, 9, '2020-09-09');
insert into bear value('ddd', 114516);
insert into bear value('dd', 114515);
insert into bear value('d', 114515);
insert into Account value(114514, 'A', 1919, '2021-10-10');
insert into Account value(114515, 'C', 1920, '2020-10-10');
insert into Account value(114516, 'B', 1919, '2020-10-10');
insert into Saving_Account value(114514, 10, 'USD');
insert into Saving_Account value(114516, 10, 'USD');
insert into Checking_Account value(114515, 10);
insert into own value('fff', 114514, '2028-05-08');
insert into own value('ff', 114514, '2028-06-08');
insert into own value('ff', 114515, '2029-01-08');
insert into Checking value('fff', 'B', 1);
insert into Checking value('ff', 'B', 1);
insert into Checking value('ff', 'C', 2);
insert into Service value('ff', '1', 'A');
insert into Service value('e', '1', 'A');
insert into Service value('ddd', '2', 'B');
