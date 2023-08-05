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
      inherit (poetry2nix.legacyPackages.${system}) mkPoetryApplication;
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      packages = {
        urlShortener = mkPoetryApplication {
          projectDir = self;
        };
        default = self.packages.${system}.urlShortener;
      };

      devShells.default = pkgs.mkShell {
        packages = [
          pkgs.python3
          poetry2nix.packages.${system}.poetry
        ];
      };
    });
}
