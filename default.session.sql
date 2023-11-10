
-- DROP TABLE "category_menu";

-- DROP TABLE "cuisine";

-- DROP TABLE "cuisine_menu";

-- DROP TABLE "category";



-- DROP TABLE "menu_items";


-- CREATE TABLE "menu_items" (
--   "id" SERIAL PRIMARY KEY,
--   "title" varchar(256) UNIQUE NOT NULL,
--   "description" varchar(2048) NOT NULL,
--   "price" money NOT NULL,
--   "spicy_level" INT NOT NULL
-- );

-- CREATE TABLE "category" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar(256) UNIQUE NOT NULL
-- );

-- CREATE TABLE "cuisine" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar(256) UNIQUE NOT NULL
-- );

-- CREATE TABLE "category_menu" (
--   "id" SERIAL PRIMARY KEY,
--   "category_id" INT NOT NULL,
--   "menu_items_id" INT NOT NULL
-- );

-- CREATE TABLE "cuisine_menu" (
--   "id" SERIAL PRIMARY KEY,
--   "cuisine_id" INT NOT NULL,
--   "menu_items_id" INT NOT NULL
-- );

-- ALTER TABLE "category_menu" ADD FOREIGN KEY ("menu_items_id") REFERENCES "menu_items" ("id");

-- ALTER TABLE "category_menu" ADD FOREIGN KEY ("category_id") REFERENCES "category" ("id");

-- ALTER TABLE "cuisine_menu" ADD FOREIGN KEY ("menu_items_id") REFERENCES "menu_items" ("id");

-- ALTER TABLE "cuisine_menu" ADD FOREIGN KEY ("cuisine_id") REFERENCES "cuisine" ("id");


-- -- Insert Categories for Gemstone-themed Items
-- INSERT INTO "category" ("name") VALUES ('Breakfast');
-- INSERT INTO "category" ("name") VALUES ('Appetizer');
-- INSERT INTO "category" ("name") VALUES ('Lunch');
-- INSERT INTO "category" ("name") VALUES ('Dinner');
-- INSERT INTO "category" ("name") VALUES ('Drink');

-- -- Insert Cuisines for Gemstone-themed Items
-- INSERT INTO "cuisine" ("name") VALUES ('International');

-- -- Insert Emerald-themed Menu Items
-- INSERT INTO "menu_items" ("title", "description", "price", "spicy_level")
-- VALUES ('Emerald Salad', 'A fresh salad with emerald greens, avocado, and a zesty emerald dressing.', 12.99, 1);

-- INSERT INTO "menu_items" ("title", "description", "price", "spicy_level")
-- VALUES ('Emerald Delight Soup', 'A hearty emerald-colored soup with seasonal vegetables and herbs.', 9.99, 0);

-- INSERT INTO "menu_items" ("title", "description", "price", "spicy_level")
-- VALUES ('Emerald Shrimp Scampi', 'Delicious shrimp scampi served with emerald-infused linguine.', 14.99, 2);

-- INSERT INTO "menu_items" ("title", "description", "price", "spicy_level")
-- VALUES ('Emerald Fusion Sushi', 'An exquisite fusion of emerald-themed sushi rolls with a hint of wasabi.', 16.99, 3);

-- INSERT INTO "menu_items" ("title", "description", "price", "spicy_level")
-- VALUES ('Emerald Elixir Smoothie', 'A refreshing green smoothie blended with emerald fruits and vegetables.', 7.99, 0);

-- INSERT INTO "menu_items" ("title", "description", "price", "spicy_level")
-- VALUES ('Sapphire Blueberry Pancakes', 'Fluffy blueberry pancakes with a sapphire-blue syrup.', 10.99, 1);

-- INSERT INTO "menu_items" ("title", "description", "price", "spicy_level")
-- VALUES ('Ruby Red Velvet Cake', 'A luscious ruby-red velvet cake with cream cheese frosting.', 8.99, 0);

-- INSERT INTO "menu_items" ("title", "description", "price", "spicy_level")
-- VALUES ('Amber Glazed Chicken', 'Tender chicken glazed with a sweet and tangy amber sauce.', 12.99, 2);

-- INSERT INTO "menu_items" ("title", "description", "price", "spicy_level")
-- VALUES ('Diamond Steak Medley', 'Prime steak served with diamond-cut potato medley and truffle sauce.', 21.99, 3);

-- INSERT INTO "menu_items" ("title", "description", "price", "spicy_level")
-- VALUES ('Pearl Pomegranate Punch', 'A sparkling punch infused with pearl-sized pomegranate seeds.', 6.99, 0);

-- -- Associate the Gemstone-themed Menu Items with Categories and Cuisines
-- INSERT INTO "category_menu" ("category_id", "menu_items_id") VALUES (1, 1);
-- INSERT INTO "category_menu" ("category_id", "menu_items_id") VALUES (2, 2);
-- INSERT INTO "category_menu" ("category_id", "menu_items_id") VALUES (3, 3);
-- INSERT INTO "category_menu" ("category_id", "menu_items_id") VALUES (3, 4);
-- INSERT INTO "category_menu" ("category_id", "menu_items_id") VALUES (4, 5);

-- INSERT INTO "cuisine_menu" ("cuisine_id", "menu_items_id") VALUES (1, 1);
-- INSERT INTO "cuisine_menu" ("cuisine_id", "menu_items_id") VALUES (1, 2);
-- INSERT INTO "cuisine_menu" ("cuisine_id", "menu_items_id") VALUES (1, 3);
-- INSERT INTO "cuisine_menu" ("cuisine_id", "menu_items_id") VALUES (1, 4);
-- INSERT INTO "cuisine_menu" ("cuisine_id", "menu_items_id") VALUES (1, 5);


INSERT INTO "cuisine_menu" ("cuisine_id", "menu_items_id") VALUES (1, 6);
INSERT INTO "cuisine_menu" ("cuisine_id", "menu_items_id") VALUES (1, 7);
INSERT INTO "cuisine_menu" ("cuisine_id", "menu_items_id") VALUES (1, 8);
INSERT INTO "cuisine_menu" ("cuisine_id", "menu_items_id") VALUES (1, 9);
INSERT INTO "cuisine_menu" ("cuisine_id", "menu_items_id") VALUES (1, 10);

INSERT INTO "category_menu" ("category_id", "menu_items_id") VALUES (1, 6);
INSERT INTO "category_menu" ("category_id", "menu_items_id") VALUES (4, 7);
INSERT INTO "category_menu" ("category_id", "menu_items_id") VALUES (4, 8);
INSERT INTO "category_menu" ("category_id", "menu_items_id") VALUES (4, 9);
INSERT INTO "category_menu" ("category_id", "menu_items_id") VALUES (5, 10);

UPDATE category_menu SET category_id = 5 WHERE id = 5
