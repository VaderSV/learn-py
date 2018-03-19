##LEGB Rule.

**L Local**— Names assigned in any way within a function (def or lambda)), and not declared global in that function.

**E Enclosing-function locals** — Name in the local scope of any and all statically enclosing functions (def or lambda), from inner to outer.

**G Global (module)** — Names assigned at the top-level of a module file, or by executing a global statement in a def within the file.

**B Built-in (Python)** — Names preassigned in the built-in names module : open,range,SyntaxError,...


![Legb Rule](https://sebastianraschka.com/images/blog/2014/scope_resolution_legb_rule/scope_resolution_1.png)