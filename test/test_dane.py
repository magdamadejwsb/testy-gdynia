from dane import wczytaj_dane


def test_wczytaj_dane(tmp_path, monkeypatch):
    folder = tmp_path / "data"
    folder.mkdir()

    plik = folder / "pogoda.csv"
    plik.write_text(
        "miasto,temp_max\nSzczecin,22\nWarszawa,20",
        encoding='utf-8'
    )

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("builtins.input", lambda _: "1")

    df = wczytaj_dane()

    assert df is not None
    assert len(df) == 2