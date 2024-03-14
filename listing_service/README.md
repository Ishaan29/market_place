# API Endpoints

## 1. Create a New Listing

- **POST** `/listings`
  - **Description**: Allows sellers to create a new listing with details about the commodity.
  - **Request Body**: Includes details like name, description, price, quantity, category, images, etc.
  - **Response**: Returns the created listing with a unique listing ID.

## 2. Retrieve All Listings

- **GET** `/listings`
  - **Description**: Retrieves a list of all available listings, with optional query parameters for filtering, sorting, and pagination.
  - **Query Parameters**: `category`, `minPrice`, `maxPrice`, `sortBy`, `page`, `limit`, etc.
  - **Response**: A paginated list of listings, each with its details.

## 3. Retrieve a Single Listing

- **GET** `/listings/{id}`
  - **Description**: Retrieves detailed information about a specific listing.
  - **Path Parameters**: `id` (the unique identifier for the listing)
  - **Response**: Detailed information about the listing.

## 4. Update a Listing

- **PUT** `/listings/{id}`
  - **Description**: Allows sellers to update the details of an existing listing.
  - **Path Parameters**: `id` (the unique identifier for the listing)
  - **Request Body**: Fields that can be updated, such as name, description, price, quantity, etc.
  - **Response**: The updated listing details.

## 5. Delete a Listing

- **DELETE** `/listings/{id}`
  - **Description**: Allows sellers to delete their listing.
  - **Path Parameters**: `id` (the unique identifier for the listing)
  - **Response**: Confirmation of deletion.

## 6. Search Listings

- **GET** `/listings/search`
  - **Description**: Search listings based on various criteria like text, category, price range, etc.
  - **Query Parameters**: `query` (search term), `category`, `priceRange`, etc.
  - **Response**: List of listings that match the search criteria.



# Listing Service Schema

| Field        | Type                          | Description                                             |
|--------------|-------------------------------|---------------------------------------------------------|
| `_id`        | ObjectId                      | Automatically generated unique identifier               |
| `title`      | String                        | Title of the listing                                    |
| `description`| String                        | Description of the listing                              |
| `price`      | Number                        | Price of the item                                       |
| `quantity`   | Number                        | Quantity available                                      |
| `category`   | String                        | Category of the item                                    |
| `sellerId`   | ObjectId                      | Reference to the seller's user document                 |
| `images`     | Array of strings              | Array of image URLs                                     |
| `createdAt`  | ISODate                       | Timestamp of when the listing was created               |
| `updatedAt`  | ISODate                       | Timestamp of when the listing was last updated          |
| `tags`       | Array of strings              | Search tags                                             |
| `isActive`   | Boolean                       | Indicates if the listing is active                      |
