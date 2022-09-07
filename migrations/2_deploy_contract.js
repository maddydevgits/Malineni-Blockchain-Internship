const Migrations = artifacts.require("hotel");

module.exports = function (deployer) {
  deployer.deploy(Migrations);
};
