const domain = require("supertest")("http://barru.pythonanywhere.com");
const expect = require("chai").expect;

describe("Scenario Register Feature", function () {
  it("Sukses ketika ada data user yang tersimpan di DB.", async function () {
    const response = await domain.get("/list-user").send({
      email: "herususeno@gmail.com",
    });

    expect(response.body.status).to.eql("SUCCESS_USER_LIST");
    expect(response.body.message).to.eql("List of registered users");
    expect(response.statusCode).to.equal(200);
    expect(response.body).to.include.keys(
      "data",
      "message",
      "status",
      "pagination"
    );
  });

  it("Sukses ketika tidak ada data user tersimpan di DB", async function () {
    const response = await domain.get("/list-user").send({
      email: "herususe@gmail.com",
    });

    expect(response.body.status).to.eql("SUCCESS_USER_LIST");
    expect(response.body.message).to.eql("List of registered users");
    expect(response.statusCode).to.equal(200);
    expect(response.body).to.include.keys(
      "data",
      "message",
      "status",
      "pagination"
    );
  });
});
