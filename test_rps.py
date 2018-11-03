import rps, pytest, subprocess, sys

def test_rock_is_valid_play():
    assert rps.is_valid_play('rock') is True # ověří, že fce vrací přesně True

def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True # 1 is True vrací False

def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True

def test_invalid_play():
    assert rps.is_valid_play('lizard') == False

def test_computer_play_is_valid():
    for _ in range(2000):
        play = rps.generate_computer_play()
        assert rps.is_valid_play(play)

def test_computer_plays_randomly():
    plays = [rps.generate_computer_play()
            for _ in range(5000)]

    assert plays.count('rock') > 200
    assert plays.count('paper') > 200
    assert plays.count('scissors') > 200

def test_paper_beats_rock():
    result = rps.evaluate_game('paper', 'rock')
    assert result == 'human'

    result = rps.evaluate_game('rock', 'paper')
    assert result == 'computer'

def test_rock_beats_scissors():
    result = rps.evaluate_game('rock', 'scissors')
    assert result == 'human'

    result = rps.evaluate_game('scissors', 'rock')
    assert result == 'computer'

def test_scissors_beats_paper():
    result = rps.evaluate_game('scissors', 'paper')
    assert result == 'human'

    result = rps.evaluate_game('paper', 'scissors')
    assert result == 'computer'

def input_faked_rock(prompt):
    """Acts like input(prompt), but instead of waiting for user input,
    assumes the user said 'rock'"""
    print(prompt)
    return 'rock'

# @pytest.fixture
# def fake_input_rock(monkeypatch):
#     monkeypatch.setattr('builtins.input', input_faked_rock)

def test_full_game(capsys):
    rps.main(input=input_faked_rock)
    captured = capsys.readouterr()
    assert 'rock, paper or scissors? ' in captured.out


def test_wrong_play_results_in_repeated_question():
    cp = subprocess.run(['python', 'rps.py'],
    encoding='utf-8',
    stdout=subprocess.PIPE,
    input='dragon\nrock\n',
    check=True)

    assert cp.stdout.count('rock, paper or scissors? ') == 2

# def input_faked_paper(prompt):
#     print(prompt)
#     return 'paper'
#
# def test_full_game_paper(capsys, monkeypatch):
#     monkeypatch.setattr('builtins.input', input_faked_paper)
#     rps.main()
#     captured = capsys.readouterr()
#     assert 'rock, paper or scissors? ' in captured.out
