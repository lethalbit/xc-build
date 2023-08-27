# XC-Build


XC-Build is a tool much like [Crosstool-NG](https://crosstool-ng.github.io/) in the sense that it helps with the building of cross-compilation toolchains. However XC-Build differs in the key sense that it helps you also manage them, and keep them up to date.

> **Note** XC-Build is **NOT** a replacement for Crosstool-NG, while
> they both build cross-compiling toolchains XC-Build is more geared
> to purely embedded and bare-metal use-cases. So it may be unsuitable
> for producing a toolchain for other purposes. However contributions
> to make it more fit for purpose are more than welcome!

## XC-Build support matrix

Symbol Key:

| Symbol | Meaning                  | Symbol | Meaning                       |
|:------:|--------------------------|:------:|-------------------------------|
| ✖️     | Does not currently build | ✔️     | Builds and is known working   |
| ❔     | Builds, not been tested  | 🚫     | Not applicable for the target |

<table>
	<thead>
	<tr></tr>
	<tr>
		<th rowspan="5">Target</th>
		<th colspan="8">Components</th>
	</tr>
	<tr></tr>
	<tr>
		<th rowspan="3">binutils</th>
		<th rowspan="3">gdb</th>
		<th rowspan="3">gcc</th>
		<th rowspan="3">standalone</th>
		<th colspan="4">libc</th>
	</tr>
	<tr></tr>
	<tr>
		<th>glibc</th>
		<th>newlibc</th>
		<th>ulibc</th>
		<th>other</th>
	</tr>
	</thead>
	<tbody>
	<tr>
		<td><code>aarch64-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>aarch64-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>aarch64-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>arm-none-eabi</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>arm-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>avr</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
		<td align="center">avr-libc</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>frv-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>frv-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>frv-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ia64-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ia64-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ia64-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>microblaze-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>microblaze-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>microblaze-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>mips-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>mips-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>mips-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>mips64-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>mips64-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>mips64-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>m68k-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>m68k-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>m68k-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>lm32-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppcle-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppcle-none-eabi</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppcle-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppcle-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppc-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppc-none-eabi</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppc-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppc-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppc64le-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppc64le-none-eabi</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppc64le-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppc64le-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppc64-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppc64-none-eabi</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppc64-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>ppc64-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>rv32-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>rv32-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>rv32-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>rv64-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>rv64-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>rv64-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>rx-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>rx-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>rx-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>s390-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>s390x-ibm-tpf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>s390x-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>sh4-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>sh4-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>sh4-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>sparc-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>sparc-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>sparc-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>sparc64-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>sparc64-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>sparc64-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>x86_64-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>x86_64-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>x86_64-unknown-linux</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="3">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>hppa-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>hppa-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>hppa64-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>hppa64-unknown-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>hppa1.1-hp-hpux10</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="4">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>hppa1.1-hp-hpux11</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="4">🚫</td>
	</tr>
	<tr></tr>
		<tr>
		<td><code>hppa2.0-hp-hpux10</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="4">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>hppa2.0-hp-hpux11</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="4">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>xtensa-none-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="4">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>xtensa-esp32-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="4">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>xtensa-lx106-elf</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="4">🚫</td>
	</tr>
	<tr></tr>
	<tr>
		<td><code>vax-linux-gnu</code></td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center">✖️</td>
		<td align="center" colspan="4">🚫</td>
	</tr>
	<tr></tr>
	</tbody>
</table>

## Parameter Expansion and Variables

The JSON definition files for the components and toolchains implement a bash-like parameter expansion with some pre-defined variables. They can be accessed using the standard `${VARIABLE}` notation. For example `--prefix=${PREFIX}`

| Variable        | Value                                                                     |
|-----------------|---------------------------------------------------------------------------|
| `VERSION`       | The current version string for the component being built                  |
| `PREFIX`        | The current toolchain prefix                                              |
| `COMMON_PREFIX` | The common component prefix. Where GMP, MPFR, MPC, et. al. are installed  |
| `HOST_TRIP`     | The host machines target triple. e.g. `x86_64-pc-linux-gnu`               |
| `TARGET_TRIP`   | The target triple of the currently being build toolchain                  |
| `SYSROOT`       | The sysroot for the currently being built toolchain                       |
| `HAS_LTO`       | Expands to `--enable-lto` if target supports LTO, otherwise is empty      |
| `INSTALL_DIR`   | Expands to the install directory for the target toolchain                 |
| `GNU_HASH`      | Expands to `--with-linker-hash-style=gnu` on targets that support it      |

There is also a collection of compound variables:

| Variable        | Value                                                                     |
|-----------------|---------------------------------------------------------------------------|
| `COMMON_BIN`    | Is equivalent to `${COMMON_PREFIX}/bin`                                   |
| `COMMON_LIB`    | Is equivalent to `${COMMON_PREFIX}/lib`                                   |
| `PLAT_BIN`      | Is equivalent to `${PREFIX}/bin`                                          |
| `PLAT_LIB`      | Is equivalent to `${PREFIX}/lib`                                          |
| `SYS_LOCAL`     | Is equivalent to `${SYSROOT}/local`                                       |
| `WITH_GMP`      | Expands to `--with-gmp=${COMMON_PREFIX}`                                  |
| `WITH_MPFR`     | Expands to `--with-mpfr=${COMMON_PREFIX}`                                 |
| `WITH_MPC`      | Expands to `--with-mpc=${COMMON_PREFIX}`                                  |
| `WITH_SYSROOT`  | Expands to `--with-sysroot=${SYSROOT}`                                    |
| `PLAT_RPATH`    | Expands to `-Wl,-rpath,${PREFIX}/lib`                                     |
| `COMMON_RPATH`  | Expands to `-Wl,-rpath,${COMMON_PREFIX}/lib`                              |



## License
XC-Build licensed under the [BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html), the full text of which can be found in the [`LICENSE`](./LICENSE) file.
