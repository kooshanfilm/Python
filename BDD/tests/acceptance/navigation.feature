Feature: Test navigation between pages
  we can have a longer description
  that can span a few lines


  Scenario: Homepage can go to Blog
    Given im on the homepage
    When I click on the line with id "blog-link"
    Then I am on the blog page


  Scenario: blog can go to HomePage
    Given im on the blogpage
    When I click on the line with id "home-link"
    Then I am on the HomePage