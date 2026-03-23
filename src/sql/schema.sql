CREATE TABLE IF NOT EXISTS USEDCARS_POSTINGS (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    posting_link VARCHAR(255) NOT NULL,
    image_link VARCHAR(255) NOT NULL,
    mileage INT,
    location_tag VARCHAR(255),
    price INT
    recentness INT
);