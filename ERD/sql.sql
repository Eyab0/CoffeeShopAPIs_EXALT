CREATE TABLE `Emp`
(
    `id`            INT          NOT NULL AUTO_INCREMENT,
    `name`          VARCHAR(255) NOT NULL,
    `phone_number`  VARCHAR(255) NOT NULL UNIQUE,
    `date_of_birth` DATE         NOT NULL,
    `address`       VARCHAR(255),
    `city`          VARCHAR(255) NOT NULL,
    `join_date`     VARCHAR(255) NOT NULL,
    `role`          VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE Order
(
    id          INT      NOT NULL AUTO_INCREMENT,
    emp_id      INT      NOT NULL,
    date_time   DATETIME NOT NULL,
    description TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (emp_id) REFERENCES Emp (id)
);

CREATE TABLE `Item`
(
    `id`   INT          NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `cost` FLOAT        NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `Customer`
(
    `id`           INT NOT NULL AUTO_INCREMENT,
    `name`         VARCHAR(255),
    `phone_number` VARCHAR(255),
    PRIMARY KEY (`id`)
);

CREATE TABLE OrderOfItems
(
    order_id    INT NOT NULL,
    item_id     INT NOT NULL,
    quantity    INT NOT NULL,
    description TEXT,
    PRIMARY KEY (order_id),
    FOREIGN KEY (order_id) REFERENCES Order (id),
    FOREIGN KEY (item_id) REFERENCES Item (id)
);



CREATE TABLE `Bill`
(
    `order_id`     INT      NOT NULL,
    `total_cost`   FLOAT    NOT NULL,
    `date_time`    DATETIME NOT NULL,
    `description`  TEXT,
    `by_emp`       INT      NOT NULL,
    `for_customer` INT      NOT NULL,
    PRIMARY KEY (`order_id`),
    FOREIGN KEY (`order_id`) REFERENCES `Order` (`id`),
    FOREIGN KEY (`by_emp`) REFERENCES `Emp` (`id`),
    FOREIGN KEY (`for_customer`) REFERENCES `Customer` (`id`)
);









