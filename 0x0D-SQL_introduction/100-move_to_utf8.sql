-- Go to UTF8
ALTER DATABASE hbtn_0c_0
CHARSET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
CONVERT TO CHARSET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
MODIFY name VARCHAR(256)
CHARSET utf8mb4
COLLATE utf8mb4_unicode_ci;
