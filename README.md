# Primaries
Primary and High Accomplishment projects... Usually with significant real world implications.

+--- Dead-Drop Program Usage and Dependencies ---+
1: Installation / Download of program files -

     1.1: Linux Users -

         1.1.1: OPTION A - Retrive Entire repo's files: (Recommended)
                         - curl -L -o repo.zip https://github.com/malachaibyrne-arch/Primaries/archive/refs/heads/main.zip && unzip repo.zip  ( <-- Copy this)

         1.1.2: OPTION B - Retrive an individual File: (Not Recommended)
                         - curl -o Deadrop-S.py https://raw.githubusercontent.com/malachaibyrne-arch/Primaries/main/Deadrop-S.py  ( <-- Copy this)
                                       ^                                                                                ^
                                       |                                                                                |
                                       |                                                                      (Name of file you want)
                                       |
                               (Name of file you want)
                        
     2.1: Windows Users -
         2.1.1: OPTION A - Windows cmd.exe Webrequest path: (Single File)
                         - Invoke-WebRequest -Uri "https://raw.githubusercontent.com/malachaibyrne-arch/Primaries/main/Deadrop-S.py" -OutFile "Deadrop-S.py"  ( <-- Copy this)
                                                                                                      (Use Filename here ^^^ )    (Use Filename here ^^^ )
                                                                                                                                                     
         2.1.2: OPTION B - Windows cmd.exe Webrequest path: (Whole Repository Downloaded + Extracted) (Recommended)
                         - Invoke-WebRequest -Uri "https://github.com/malachaibyrne-arch/Primaries/archive/refs/heads/main.zip" -OutFile "repo.zip"; Expand-Archive -Path "repo.zip" -DestinationPath "." -Force  ( <-- Copy this)
                                                                                                                                              (e.g. C:\Users\Admin\Downloads\Repositories  ^^^^)
                                                                                                                                              
3.  Back-End Package Dependencies

  3.1.  The Server and Client programs for Deadrop.py (server + Client Variations) were built for python; operating on python 3.13.14 [ 21 / 07 / 2026 ]
      3.1.1 - "pip install python" (for windwos)  ( <-- Copy this)
      3.1.2 - "sudo apt install python -y (for Debian based Linux-Distros)  ( <-- Copy this)
      3.1.3 - "yes | sudo pacman -S python" (for Arch-based Linux-Distros ( btw ))  ( <-- Copy this)
    
  3.2  Both Client and server for Deadrop.py use the socket and cryptography python libraries. Some machines, mine included, will require these dependencies to be downloaded manually.
  
      3.2.1  Ugrade 'pip' 
          3.2.1.1  - "python -m pip install --upgrade pip" ( <-- Copy this)
          
      3.2.2  Install Cryptography -
          3.2.2.1  - "pip install cryptography"   ( <-- Copy this)


+ --- Summary --- +
+ 
+ Deadrop-S.py and Deadrop-C.py Downloaded
+ Python's latest version installed
+ Cryptography Library Downloaded
+ Run Server First ( "python .\Deadrop-S.py" ) when in the directory for that file.
+ Run Client Next ( "python .\Deadrop-C.py" ) when in the directory for that file.

+ INFO -
+ Within the Cryptography Library... The Fernet module is called by both Server and Client for message Encryption.
+   Fernet uses 128-bit AES (Advanced Encryption Standard) for encryption, as well as SHA256 HMAC (Hash-based Message Authentication Code)
+   to authenticate the integrity of data parsed through the secure tunnel created by this program.
    
