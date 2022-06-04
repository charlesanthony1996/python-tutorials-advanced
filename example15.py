#writing a turing machine in python step by step

import time
from collections import defaultdict
from dataclasses import dataclass, field

@dataclass
class TuringMachine:
    states: set[str]
    symbols: set[str]
    blank_symbol: str
    input_symbol: set[str]
    intial_state: str
    accepting_states: set[str]
    transitions: dict[tuple[str, str], tuple[str, int]]
    #state symbol -> new state , new symbol , direction


    head: int = field(init=False)
    tape = defaultdict[int, str] = field(init=False)
    current_state: str = field(init=False)
    halted: bool = field(init=False, default=False)

    def initialize(self, input_symbols:dict[int, str]):
        self.head = 0
        self.halted = False
        