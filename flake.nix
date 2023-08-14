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
      poetryPkgs = poetry2nix.legacyPackages.${system};

      pythonEnv = mkPoetryEnv {
        python = pkgs.python311;
        pyproject = ./pyproject.toml;
        poetrylock = ./poetry.lock;
        overrides =
          poetryPkgs.overrides.withDefaults
          (self: super: {
            django-browser-reload =
              super.django-browser-reload.overridePythonAttrs
              (
                old: {
                  buildInputs = (old.buildInputs or []) ++ [super.setuptools];
                }
              );

            django-libsass =
              super.django-libsass.overridePythonAttrs
              (
                old: {
                  buildInputs = (old.buildInputs or []) ++ [super.setuptools];
                }
              );
          });
      };
    in {
      packages = {
        urlShortener = mkPoetryApplication {
          projectDir = self;
          inherit python;
        };
        default = self.packages.${system}.urlShortener;
      };

      devShells.default = pkgs.mkShell {
        packages = [
          pythonEnv
          python
          poetry2nix.packages.${system}.poetry
          pkgs.litecli
        ];
      };
    });
}
