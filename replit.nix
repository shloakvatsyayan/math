{ pkgs }: {
    deps = [
      pkgs.nano
      pkgs.ungoogled-chromium
      pkgs.chromedriver
      pkgs.geckodriver
      pkgs.openai
      pkgs.unzip
      pkgs.cowsay
    ];
}