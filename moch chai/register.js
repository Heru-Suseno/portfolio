const domain = require("supertest")("http://barru.pythonanywhere.com");
const expect = require("chai").expect;

describe("Scenario Register Feature", function () {
  it("Berhasil Register, dengan valid email and password", async function () {
    const response = await domain.post("/register").send({
      email: "herususeno@gmail.com",
      password: "12345",
      name: "heru",
    });

    expect(response.body.data).to.eql("berhasil");
    expect(response.body.status).to.eql("SUCCESS_REGISTER");
    expect(response.body.message).to.eql("created user!");
    expect(response.statusCode).to.equal(200);
    expect(response.body).to.include.keys("data", "message", "status");
  });

  it("Gagal registrasi, sudah ada email terdaftar.", async function () {
    const response = await domain.post("/register").send({
      email: "herususeno@gmail.com",
      password: "12345",
      name: "heru",
    });

    expect(response.body.data).to.eql(
      "Email sudah terdaftar, gunakan Email lain"
    );
    expect(response.body.status).to.eql("FAILED_REGISTER");
    expect(response.body.message).to.eql("Gagal Registrasi");
    expect(response.statusCode).to.equal(420);
    expect(response.body).to.include.keys("data", "message", "status");
  });

  it("Gagal registrasi, email/username/password kosong.", async function () {
    const response = await domain.post("/register").send({
      email: " ",
      password: " ",
      name: " ",
    });

    expect(response.body.data).to.eql(
      "Email/Username/Password tidak boleh kosong"
    );
    expect(response.body.status).to.eql("FAILED_REGISTER");
    expect(response.body.message).to.eql("Gagal Registrasi");
    expect(response.statusCode).to.equal(420);
    expect(response.body).to.include.keys("data", "message", "status");
  });

  it("Gagal registrasi, email tidak valid, harus……@..........com.", async function () {
    const response = await domain.post("/register").send({
      email: "heru",
      password: "heru",
      name: "heru",
    });

    expect(response.body.data).to.eql("Email tidak valid");
    expect(response.body.status).to.eql("FAILED_REGISTER");
    expect(response.body.message).to.eql("Cek kembali email anda");
    expect(response.statusCode).to.equal(420);
    expect(response.body).to.include.keys("data", "message", "status");
  });

  it("Gagal registrasi, username mengandung simbol", async function () {
    const response = await domain.post("/register").send({
      email: "heruuu@gmail.com",
      password: "heru",
      name: "heru*",
    });

    expect(response.body.data).to.eql("Password tidak valid");
    expect(response.body.status).to.eql("FAILED_REGISTER");
    expect(response.body.message).to.eql("Tidak boleh mengandung symbol");
    expect(response.statusCode).to.equal(420);
    expect(response.body).to.include.keys("data", "message", "status");
  });

  it("Gagal registrasi, password mengandung simbol", async function () {
    const response = await domain.post("/register").send({
      email: "heruuuu@gmail.com",
      password: "heru!!!",
      name: "heru",
    });

    expect(response.body.data).to.eql("Password tidak valid");
    expect(response.body.status).to.eql("FAILED_REGISTER");
    expect(response.body.message).to.eql("Tidak boleh mengandung symbol");
    expect(response.statusCode).to.equal(420);
    expect(response.body).to.include.keys("data", "message", "status");
  });
});
