# Tabibito Travel Website

## 1. Introduction
**Tabibito** is a unique travel website offering a wide range of domestic and international tours. With detailed itineraries, cost information, and visual aids like pictures and maps, users can easily plan their trips. The website features a smart chat function for live assistance and personalized customer service. Users can also contribute reviews and ratings to help fellow travelers. Our website is committed to providing affordable tours without compromising on safety and quality. The goal is to make travel comfortable and memorable for users by offering a comprehensive one-stop travel service.

## 2. Technologies
To implement the website and fulfill the requirements, the following technologies are used:

### 2.1 Languages:
- Python
- HTML
- CSS
- JavaScript

### 2.2 Basic Technologies:
- **Vue.js**: A flexible JavaScript framework that enables the use of beautiful and powerful external component libraries by breaking web pages into reusable components.
- **Flask**: A lightweight web application framework based on Python, allowing for flexible and convenient development, reducing time and resource costs.
- **MySQL**: An open-source relational database management system (RDBMS) that uses SQL to manage data, providing a solid data security layer.

### 2.3 External Libraries:
- **Naive UI**: A Vue 3 Component Library with theme-customization features.
- **i18n**: An internationalization framework for JavaScript.
- **Tencent Instant Messaging**: A mature instant messaging solution provided by Tencent.
- **ChatGPT API**: Provides access to OpenAI’s advanced large-scale language model, ChatGPT.
- **Google Map JavaScript API**: Integrates Google Map and Google Street View into the website.
- **Echarts**: An open-source JavaScript visualization library for creating interactive data visualizations.
- **FlightAware Aero API**: Provides access to flight information from all over the world.
- **Weather API**: Provides access to weather information from various locations globally.

## 3. Requirements

### 3.1 Functional Requirements:
- **Customer Portal**: Allows customers to browse travel program details, publish and view comments, modify personal profiles, reserve travel programs, communicate with staff, and modify reservation information.
- **Staff Portal**: Allows staff to manage reservations and travel program information, upload new travel programs, send announcements to customers, and answer customer queries.
- **Innovative Functions**: Includes maps and street views, AI chat service, data visualizations, weather and flight inquiry services, travel video introductions, and efficient program recommendations.

### 3.2 Non-Functional Requirements:
- **Performance**: The system must handle heavy loads and provide fast response times.
- **Security**: The system must secure and protect user data through encryption and access controls.
- **Maintainability**: The system must be modular and well-documented for ease of maintenance.
- **Usability**: The system must be user-friendly, providing helpful resources and a responsive interface.

## 4. Design & Solution

### 4.1 Functional Requirement Implementation - Customer Side

#### 4.1.1 Maps and Street Views
- **User Story**: As a traveler, I want to see a map showing all the sites in a travel program so I can better understand the program.
- **Solution**: 
    - **Front-end**: A Google Map is provided for each travel program to give an overview of the sites.
    - **Back-end**: The front end requests map information, which is used to retrieve the map image from the Google Map API.

#### 4.1.2 Data Visualizations: Footprint Wall, Heat Maps, and Charts
- **User Story**: As a customer, I want to view my travel records and information about tourist attractions in a visually appealing way.
- **Solution**: Integrates **Echarts** to display user travel records and tourist attraction heat maps.

#### 4.1.3 Efficient Travel Recommendation Service
- **User Story**: As a user, I want a travel recommendation service that provides relevant suggestions based on my interests.
- **Solution**: A recommendation service using user-based and content-based collaborative filtering algorithms.

#### 4.1.4 Diversified Display of Program Information
- **User Story**: As a travel customer, I want to view detailed travel product information in different formats, including media like photos and videos.
- **Solution**: Each travel program page contains text descriptions, photos, videos, and 3D model demonstrations for intuitive understanding.

#### 4.1.5 Browse Travel Program Details
- **User Story**: As a customer, I want to view detailed travel destination information like price, pictures, itineraries, and dates.
- **Solution**: A dedicated page for each travel program displays all necessary details, including 3D models made with Blender.

#### 4.1.6 Publish and View Comments on a Travel Program
- **User Story**: As a customer, I want to publish comments on a travel program to share my experiences.
- **Solution**: Customers can submit comments using a form with ratings, titles, and descriptions, displayed on the travel program page.

#### 4.1.7 View Basic Information about the Travel Agency (About Us Page)
- **User Story**: As a customer, I want to learn about the website's background and team to assess its credibility.
- **Solution**: An "About Us" page that provides company and team information, service introduction, and user feedback, using a clean, responsive design.

#### 4.1.8 Modify Personal Profile
- **User Story**: As a customer, I want to modify my personal profile information.
- **Solution**: A personal profile page where users can edit and save their profile information.

#### 4.1.9 Weather and Flight Inquiry Services
- **User Story**: As a customer, I want to check flight and weather information for my destination.
- **Solution**: Uses the **FlightAware Aero API** for flight details and **Free Weather API** for weather data.

#### 4.1.10 Reserve Travel Programs
- **User Story**: As a customer, I want to reserve a travel program.
- **Solution**: After booking, the reservation is sent to the back end to be stored in **MySQL**.

### 4.2 Functional Requirement Implementation - Staff Side

#### 4.2.1 View Dashboard
- **User story**: As a staff, I would like to view the website’s revenue situation and latest booking orders in a more intuitive way so that I can better understand the website’s performance and manage operations.
- **Solution**: A dashboard is provided for employees to view data visualization charts showing the website’s revenue and latest booking orders.

#### 4.2.2 Reservation and Travel Programs Table Management
- **User story**: As a staff, I want to efficiently view, modify, and delete information related to orders and travel programs.
- **Solution**: MVC architecture handles reservations and travel programs through the employee portal. Staff can modify the order status in real time.

#### 4.2.3 Edit and Send Notification to Customers
- **User story**: As a staff, I want to edit and send notifications to customers quickly to save time.
- **Solution**: The front end allows staff to edit and send notifications after modifying travel programs. Notifications consist of a title, type, status, and content.

#### 4.2.4 Upload New Travel Programs
- **User story**: As a travel agency staff, I want to upload travel destination information like the name, pictures, location, and price for customers to book.
- **Solution**: A form is created for staff to input necessary information about travel destinations. The information is stored in a MySQL database.

#### 4.2.5 Epidemic Management
- **User story**: As a travel agency staff, I want to manage reservation statuses during the pandemic to protect customer safety.
- **Solution**: A reservation management system using Flask and MySQL allows staff to update and manage reservation statuses.

### 4.3 Functional Requirement Implementation - Customer and Staff Side

#### 4.3.1 Login and Register
- **User story**: As a customer, I want to access personalized services with my account.
- **Solution**: Users can sign in via Google or sign up with a new account. The system sends a unique verification code for email validation.

#### 4.3.2 Track Reservation Status
- **User story**: As a customer or staff, I want to track my reservations and stay updated on any changes.
- **Solution**: Customers and staff can track reservation statuses on the website.

#### 4.3.3 Modify Reservation Status
- **User story**: As a customer, I want to modify or cancel reservations to have better control over my travel plans.
- **Solution**: Staff can modify or cancel reservations through the staff management’s order page. Customers can view and manage their own reservations.

#### 4.3.4 AI Customer Service
- **User story**: As a customer or staff, I want to quickly find information and get my questions answered without navigating through multiple pages.
- **Solution**: Integrated OpenAI GPT-4 to provide natural language processing for customer queries via a chatbot interface.

#### 4.3.5 Chat Between Customer and Staff
- **User story**: As a customer or staff, I want to have immediate online chats for more details about travel information.
- **Solution**: Integrated Tencent Cloud’s instant messaging service (IMS) for real-time chats between customers and staff.

#### 4.3.6 Chinese-English Switching
- **User story**: As a customer or staff, I want to view the website in my preferred language.
- **Design & Solution**:
  - Integrated `vue-i18n` library to support language switching between Chinese and English.
  - The system uses `.json` files to store the corpus for each language, allowing easy adaptation.

## 4.4 Non-Functional Requirement Implementation

### Performance
- Implemented optimization techniques such as Vue lazy loading to ensure system performance under heavy load.

### Security
- Implemented password encryption and authority management to ensure system and data security.

### Maintainability
- Modular design principles and extensive code documentation ensure ease of maintenance and modification.
- Component-based design improves code reusability.

### Usability
- Conducted extensive user testing and implemented a user-friendly interface with comprehensive documentation.

---

For more details, refer to the full project system and user documentation.
