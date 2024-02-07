describe("general navigation", () => {
  it("navigates the staging website", () => {
    cy.visit("https://staging.museumofdreamworlds.org/");

    cy.contains("Museum of Dreams");
  });
});
