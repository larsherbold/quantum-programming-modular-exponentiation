# Implementation of Modular Exponentiation in Qiskit
This project focuses on building a quantum circuit for modular exponentiation from scratch, a critical subroutine used in Shor's period-finding algorithm for integer factorization. Developed for the [QPROG](https://utbildning.su.se/english/education/course-catalogue/ml/ml730n) course at the Department of Computer and Systems Sciences, Stockholm University, the implementation follows a modular bottom-up approach. Starting from basic reversible logic gates such as X, CNOT, CCNOT, and Multicontrolled-NOT, the project constructs complex arithmetic components including full adders, subtractors, and comparison circuits to ultimately perform multiplication and exponentiation modulo $N$.

## Authors
- Lea Jesenkovic
- Lars Herbold

## Install
```bash
git clone https://github.com/larsherbold/quantum-programming-modular-exponentiation.git
cd quantum-programming-modular-exponentiation
```

```bash
python3 -m venv venv
```

* On Linux/macOS:
```bash
source venv/bin/activate
```
* On Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

```bash
pip install -r requirements.txt
```
