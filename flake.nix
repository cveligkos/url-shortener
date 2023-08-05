{
  description = "Application packaged using poetry2nix";

  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  inputs.poetry2nix = {
    url = "github:nix-community/poetry2nix";
    inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    poetry2nix,
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      inherit (poetry2nix.legacyPackages.${system}) mkPoetryApplication mkPoetryEnv;
      pkgs = nixpkgs.legacyPackages.${system};
      python = pkgs.python311;
      pythonEnv = mkPoetryEnv {
        inherit python;
        pyproject = ./pyproject.toml;
        poetrylock = ./poetry.lock;
      };
    in {
      packages = {
        urlShortener = mkPoetryApplication {
          projectDir = self;
        };
        default = self.packages.${system}.urlShortener;
      };

      devShells.default = pkgs.mkShell {
        buildInputs = [
          pythonEnv
        ];

        packages = [
          python

          poetry2nix.packages.${system}.poetry
        ];
      };
    });
}
