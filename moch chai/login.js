const domain = require("supertest")("http://barru.pythonanywhere.com");
const expect = require("chai").expect;

describe("Scenario Login Feature", function () {
  it("Berhasil Login, dengan valid email and password", async function () {
    const response = await domain
      .post("/login")
      .send({ email: "herususeno@gmail.com", password: "12345" });

    expect(response.body.status).to.eql("SUCCESS_LOGIN");
    expect(response.body.message).to.eql("Anda Berhasil Login");
    expect(response.statusCode).to.equal(200);
    expect(response.body).to.include.keys(
      "data",
      "message",
      "status",
      "credentials"
    );
  });

  it("Gagal login, data tidak ditemukan di Data Base.", async function () {
    const response = await domain
      .post("/login")
      .send({ email: "herususenoo@gmail.com", password: "12345" });

    expect(response.body.status).to.eql("FAILED_LOGIN");
    expect(response.body.message).to.eql("Email atau Password Anda Salah");
    expect(response.statusCode).to.equal(420);
    expect(response.body).to.include.keys(
      "data",
      "message",
      "status"
    );
  });


  it("Gagal login, email tidak valid …..@......com.", async function () {
    const response = await domain
      .post("/login")
      .send({ email: "herususeno", password: "12345" });

    expect(response.body.status).to.eql("FAILED_LOGIN");
    expect(response.body.message).to.eql("Cek kembali email anda");
    expect(response.body.data).to.eql("Email tidak valid");
    expect(response.statusCode).to.equal(420);
  });

  it("Gagal login, email melebihi max karakter", async function () {
    const response = await domain
      .post("/login")
      .send({ email: 
        "herususenoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo@gmail.com", 
        password: "12345" });

    expect(response.body.status).to.eql("FAILED_LOGIN");
    expect(response.body.message).to.eql("Email/Password melebihin maksimal karakter");
    expect(response.body.data).to.eql("Cek Formulir Anda");
    expect(response.statusCode).to.equal(200);
    expect(response.body).to.include.keys(
      "data",
      "message",
      "status",
    );
  });

  it("Gagal login, password menggunakan spasi", async function () {
    const response = await domain
      .post("/login")
      .send({ email: 
        "herususeno@gmail.com", 
        password: "1234 5" });

    expect(response.body.status).to.eql("FAILED_LOGIN");
    expect(response.body.message).to.eql("Email atau Password Anda Salah");
    expect(response.body.data).to.eql("User's not found");
    expect(response.statusCode).to.equal(420);
    expect(response.body).to.include.keys(
      "data",
      "message",
      "status",
    );
  });

  it("Gagal login, password menggunakan simbol", async function () {
    const response = await domain
      .post("/login")
      .send({ email: 
        "herususeno@gmail.com", 
        password: "12345!!!" });

    expect(response.body.status).to.eql("FAILED_LOGIN");
    expect(response.body.message).to.eql("Tidak boleh mengandung symbol");
    expect(response.body.data).to.eql("Password tidak valid");
    expect(response.statusCode).to.equal(420);
    expect(response.body).to.include.keys(
      "data",
      "message",
      "status",
    );
  });

  });