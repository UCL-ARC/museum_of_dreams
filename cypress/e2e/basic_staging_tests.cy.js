describe("general navigation", () => {
  it("navigates the staging website", () => {
    // cy.visit("http://museumofdreams.eu-west-2.elasticbeanstalk.com/"); // for whatever reason it times out when accessing the proper staging site

    cy.visit("localhost:1080");

    cy.contains("STAGING");

    cy.get("#menu-icon").click();
    cy.contains("Analyses: Critical Essays and Discussions").click();

    cy.contains("Critical discussions and essays on this site");
    cy.url().should("include", "/analyses");
  });
});
