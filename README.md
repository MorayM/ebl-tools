# EBL file tools

A set of tools to work with (and hopefully eventually convert) E-MU `.ebl` files. Based on work by [Danny Brien](https://www.dannybrien.com/ebl/).

## Sample names

Get the sample name from an EBL file.

```shell
python get_name.py <file>.ebl
```

## TODO

- Extract all known information about a file, as documented by Danny Brien
- Extract audio as a WAV file
- Embed sample loop info in extracted WAV file
- Output [Decent Sampler](https://www.decentsamples.com/product/decent-sampler-plugin/) instrument files (see [here](https://www.decentsamples.com/docs/format-documentation.html) for details)
- Read information from Emulator X `.exb` soundbank files
