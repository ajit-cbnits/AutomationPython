from selenium.webdriver.common.by import By

class Locator:
    
#login Page Locators
    userNameElement = (By.ID,"email")
    passwordElemenmt =(By.ID,"password")
    submittButtonElement=(By.XPATH,"//button[@type='submit']")
    
    InvalidEmailerrMsg =(By.CLASS_NAME,"errorMsg")
    ErrorMessage = (By.XPATH,"//div[@id='toaster']/div[@class='alert alert-danger alert-dismissible fade show']")
    
#Home page element after valid login
    imageButton = (By.XPATH,"//img[@class='userImage']")
    LogOutButton =(By.XPATH,"//a[contains(text(),'Logout')]")
    

#Sign Up Page Element 
    createAccountLink =(By.XPATH,"//a[contains(text(),'Create account')]")
    firstName = (By.XPATH,"//input[@id='fname']")
    lastName = (By.XPATH,"//input[@id='lname']")
    emailAddress = (By.XPATH,"//input[@id='email']")
    password=(By.XPATH,"//input[@id='password']")
    confirmPassword=(By.XPATH,"//input[@id='confirmPassword']")
    CreateButton=(By.XPATH,"//button[@type='submit']")
    
#After perform sign Up LogIn should be appear 
    
    logInLink = (By.XPATH,"//a[contains(text(),'Login')]")