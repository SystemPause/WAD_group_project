

# LanguageSwap 
## Group Project: WAD2 - University of Glasgow 2018
## Group members: 

 1. Martina Cocco - 2267320C
 2. Zay Yar Tun - 2277073Z
 3. Gloria Dhandapani - 2252533D
 4. Alessandro Speggiorin - 2268690S

## Project Overview 

## Coding Syle
In this section we should add coding rules that we want follow so that we all follow the same coding standards.  

 - In every view, in order to get the url we should use the **reverse** function
 
    ```python
        reverse('news-archive')
    ```
    
    
 - In every template, in order to get the url we should use
 
    ```python
        {% url 'show_category'}
    ```
## TODO List 


## Marking Scheme

**Deployment**
- [ ] Application is deployed via PythonAnywhere and runs from there - 2
- [ ] Requirements file is included and contains the correct packages - 2
- [ ] Database / migrations files not included - 1
- [ ] Population script works and contains useful example data - 2
- [ ] Application can be deployed on marker's own machine - 2

**Functionality**
- [ ] Main functionality has been implemented reflecting the design - 10
- [ ] Application is bug-free / no error messages occur - 3
- [ ] Application includes some Javascript / JQuery / AJAX - 5

**Look and Feel**
- [ ] Polished / refined interface, not clunky - 3
- [ ] Uses a responsive CSS framework - 3
- [ ] If browser window size changed, is the change handled neatly? - 1

**Code**
- [ ] Templates inherit from base - 2
- [ ] URLs are relative, i.e., use the {% url ..%} tag - 2
- [ ] Code contains helper functions/classes (if required) - 2
- [ ] Code is readable, clear and commented where appropriate - 3
- [ ] CSS and Javascript are kept separate from templates (i.e., not inline) - 1
- [ ] No repetition of code blocks in the views or templates - 2
- [ ] Unit tests are included - 4



