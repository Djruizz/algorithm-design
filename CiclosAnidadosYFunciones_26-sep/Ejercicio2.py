def hide_pass(password):
    hidden = ""
    index = 0
    for i in password:
        if index == 1 or index == 2:
            hidden += "*"
        else:
            hidden += i
        index += 1
    return hidden

print(hide_pass("contraseñaSuperSegura"))