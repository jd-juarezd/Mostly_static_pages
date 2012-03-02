Feature: Rocking with lettuce and django

    Scenario: Prueba Home
        Given I access the url "/home/"
        Then I see the header "Sample App"

 	Scenario: Prueba Contact
        Given I access the url "/contact/"
        Then I see the header "Contact"
    
    Scenario: Prueba About
        Given I access the url "/about/"
        Then I see the header "About Us"

    
