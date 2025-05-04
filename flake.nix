{
  description = "PlatformIO development environment for Arduino/ESP32";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
  }: let
    system = "x86_64-linux"; # For multi-system support, use lib.systems.flakeExposed
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        platformio
        platformio-core.udev
        libusb1

        screen

      ];

      # Explicitly set environment variables
      env = {
        # Ensures fish is recognized as the shell
        SHELL = "${pkgs.fish}/bin/fish";
      };

      # Cleaner shell initialization (avoids 'exec' potential issues)
      shellHook = ''
        echo "Entering PlatformIO environment"
        ${pkgs.fish}/bin/fish
      '';
    };
  };
}
