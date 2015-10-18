# Introduction #

QColorScheme allows you to easily colorize your PyQt applications. Be it to integrate them with existing applications or just because you want to. It does so by modifying the application's (or widget's) pallete. Hence it only works properly with Styles (and widgets) that use the palette to draw. A non-working example would be the WindowsVista or WindowsXP styles as they use custom code to draw certain effects (like the progress bar for example) and hence do not pick up the modified palette colors.

For now i hardcoded it to use the Plastique style as this works pretty well. Others work too tho, and it is easy to change if wanted.


# Details #

The easiest way to use QColorScheme is to simply put it somewhere on your python path, import it and simply create an instance. The constructor will automatically apply the theme to the whole application by default. Also it will generate a nuke-like appearance by default (dark slate gray with an orange highlightcolor for focus indicators, progressbars etc.)

To override the default colors you can either supply colors and spread value as optiona arguments when creating the instance or setting QColorScheme.baseColor, .highlightColor and .spread manually and call QColorScheme.generateScheme (which will by default apply the scheme to the whole app).

Alternatively you can also create the instance passing the "apply=False" argument to prevent automatic styling of the application and use QColorScheme.apply(widget) to apply the scheme only to selected widgets (and all subwidgets).

More Details to follow and in the inline documentation

![http://www.leviathan-entertainment.de/wp-content/uploads/nukeScheme.jpg](http://www.leviathan-entertainment.de/wp-content/uploads/nukeScheme.jpg)
![http://www.leviathan-entertainment.de/wp-content/uploads/brightScheme.jpg](http://www.leviathan-entertainment.de/wp-content/uploads/brightScheme.jpg)