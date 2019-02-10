import certificates

gen = certificates.Certificate_Generator(
        template_filepath="/Users/ajayraj/Documents/CSI/CertificateGenerator/workshopcertificate.jpeg",
        contestants_filepath="/Users/ajayraj/Documents/CSI/CertificateGenerator/codehs.csv"
    )
gen.extract_contestants_data(positions=[(250, 425), (508, 395)])
gen.make_certificates()
gen.save_all(target_dir="/Users/ajayraj/Documents/CSI/CertificateGenerator/Target")

# Masnasa's fav song: thela cheera kataru malli pullu techanu ra-raa