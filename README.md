<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      </li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Committing Changes</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

We're trying to simulate yo

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/gitblip/Analog-Neural_Network_simulation.git
   ```

    ![pic to help](assets/images/HelpfulPicyes.png)

2. Enter the repo and change your branch to avoid pushing to main
    ```sh
    cd Analog-Neural_Network_simulation
    git switch -c <branch-name>
    ```
3. Make sure to check which branch youre pushing your update to
   ```sh
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE -->
## Committing changes

After createing a seperate and new branch, push updates to here

1. Create the .git folder (it should already have been created after cloning the repo)
    ```sh
    git init
    ```
2. After adding your changes, you need to add those changes that you want to ur init file before pushing to your branch
    ```sh
    git add .
    #this is a comment, not always ull need to add everything, sometimes u want add only seom things, figure it out if u to remove stuff from your commit or whatev is required, but beware of commit history and adding to commit before pushing the previous commit
    ```
3. Commit your changes
    ```sh
    git commit -m "whatev msg u want to display with your commit"
    git status
    #git status helps you see what files will be pushed
    ```
4. Check your branch and then push, DONT PUSH TO MAIN  
    ```sh
    git branch --show-current
    #for the first time youll need to run this
    git push -u origin <branch name>
    # '-u' sets your upstream sot hat next time onwards you can just type the following
    git push
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

