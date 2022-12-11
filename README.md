# cwds
Centralised waste disposal system 
 * User
        (four type of users)
   * Superadmin
        (super admin is main user of website who manage and maintain activities done by agency,plant,user)
      * Approval
         * Super admin conform  new registered agency,plant,user after registered in website
      * User management
         * Super admin has ability to view all registered agency ,plant, user, product created by plant, order of product done by user, change limits of users in an agency
      * Feedbacks
         * Inbox
            * Inbox contains received message from user and agency
         * Response
            * Can send response to agency
         * Sent items
            * Sent items contains response that send by admin
            * Can remove response created 
      * Add location
         * Only this location can select by agency,plant , user at registration time
         * Location can be removed and modified by superadmin
      * My account
         * Can view and edit own profile - username, password
   * Agency
        (agency provide facility to user for waste disposal who purchase plant from providers)
      * Select plant
         * Agency can select one or more plant 
      * Request pant
         * Selected plant can be requested to the plant provider
      * Processing
         * Requested plants moved to processing state until getting approval from plant provider
      * View request
         * Agency can view user request and passed to completed stage
      * Warnings
         * View warnings
            * Can view message sent by admin
         * Response
            * Response messages to admin
            * Sent items
               * Can view response sended to admin
      * My account
         * Agency can edit profile informations and change(remove) plants
      * registration/profile information
         * Name
         * Address
         * Location(locations created by admin)
         * Pincode
         * Email
         * Contact number
         * Username
         * password
   * Plant
(provider of plants of specific type)
      * View request
         * Plant provider can process request from agency (move to completed state)
      * Products
         * Each plant can create,edit, remove their own products
      * Orders
         * Plant user can manage products ordered from user(customer)
            * It has three stages processing, payment received, shipped 
            * Stages can be changed by plant user
      * My account 
         * Each plant user can modify profile information
      * registration/profile information
         * Name
         * Address
         * Location
         * Pincode
         * Email
         * Contact Number
         * Type of plant
            * Bio-degradable plant
            * Metal plant
            * Plastic plant
         * Username
         * Password
   * User
        (customer who use waste disposal system)
      * Select agency
         * User can select one agency and can change current agency to new
      * Request agency
         * Selected agency is passed to request state
         * After requesting it s moved to processing state until accepted by agency
      * Feedback
         * Create new feed back to admin
            * Have To, subject, feedback
         * Send items
            * Sent items hold created feedback it can removed by user
         * Inbox
            * Inbox contain message from agency
      * Buy products
         * Fertilizer
        (shows all products from available plant providers)
            * Product name, description, image and button to purchase(buy)
            * When purchasing product can view price and enter quantity 
         * View status
            * Purchased product status can viewed by user( processing, payment received, shipped )
      * My account
         * User can view, modify profile informations
         * Can remove agency
      * registration/profile informations
         * Name
         * Address
         * Location
         * Pin code
         * Email
         * Contact number
         * Username
         * Password
* registration/login
   * agency,plant , user have direct registration button and login page
   * Super Admin can login through separate url link
   * After registration email confirmation is needed for account activation
* Account recovery
   * Forgot password:
      * Account can recover using registered email address
* Contact form
   * (new contact visible in admin’s inbox)
   * Name
   * Email
   * Subject
   * Message 
* Donation
                (information submitted to admin inbox)
   * Donation amount
   * Donation type
      * One time
      * Monthly 
      * Yearly
   * Name
   * Email
   * Comment(about donation)
