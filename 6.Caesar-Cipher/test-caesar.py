import pytest
from caesar import transform


@pytest.mark.parametrize(
    'key, plaintext, ciphertext',
    [
        (0, 'hello, world!', 'HELLO, WORLD!'),
        (20, 'pyth0n_proj3ctz', 'JSNB0H_JLID3WNT'),
    ],
)
def test_keys_between_0_and_25_encrypt_correctly(key, plaintext, ciphertext):
    assert transform('encryption', key, plaintext) == ciphertext


@pytest.mark.parametrize(
    'key, ciphertext, plaintext',
    [
        (15, 'ADGTB XEHJB SDADG', 'LOREM IPSUM DOLOR'),
        (18, 'Z3J3 T3 VJ*YGFK', 'H3R3 B3 DR*GONS'),
    ],
)
def test_keys_between_0_and_25_decrypt_correctly(key, ciphertext, plaintext):
    assert transform('decryption', key, ciphertext) == plaintext


@pytest.mark.parametrize(
    'key, plaintext, ciphertext',
    [
        (27, 'put ev3ryth1ng on a _Bagel!', 'QVU FW3SZUI1OH PO B _CBHFM!'),
        (3000, 'an everything BAGEL!', 'KX OFOBIDRSXQ LKQOV!'),
    ]
)
def test_keys_greater_than_26_encrypt_correctly(key, plaintext, ciphertext):
    assert transform('encryption', key, plaintext) == ciphertext


@pytest.mark.parametrize(
    'key, ciphertext, plaintext',
    [
        (890, '1 YNKKV, 2 YNKKV, 3 YN33V, 4...', '1 SHEEP, 2 SHEEP, 3 SH33P, 4...'),
        (42, ' %^&* JXQJI WYRRUHYIX ^_^', ' %^&* THATS GIBBERISH ^_^'),
    ]
)
def test_keys_greater_than_26_decrypt_correctly(key, ciphertext, plaintext):
    assert transform('decryption', key, ciphertext) == plaintext
