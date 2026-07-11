%global tl_name minibox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2a
Release:	%{tl_revision}.1
Summary:	A simple type of box for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/minibox
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minibox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minibox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minibox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small package provides a convenient input syntax for boxes that
don't break their text over lines automatically, but do allow manual
line breaks. The boxes shrink to the natural width of the longest line
they contain.

