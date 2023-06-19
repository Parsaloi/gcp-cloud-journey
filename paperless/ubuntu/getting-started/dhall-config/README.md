
# How to integrate Dhall

Surveying options for reading in Dhall configuration files

These three ways can be used to integrate the Dhall configuration language into my project:  
- Language support for reading Dhall configuration files (this is the only way to get complete support for Dhall, including invoking Dhall functions from your application)

## Language support

The following languages can read in Dhall configuration files directly using a package that natively implements Dhall:  
- Clojure - Via the ```dhall-clj``` package
- Haskell - Via the ```dhall``` package
- Go - Via the ```dhall-golang``` package
- Ruby - Via the ```dhall-ruby``` package
- Rust - Via the ````serde_dhall``` package

The following languages can read in Dhall configuration
