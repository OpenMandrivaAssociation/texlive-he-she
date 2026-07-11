%global tl_name he-she
%global tl_revision 41359

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Alternating pronouns to aid gender-neutral writing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/he-she
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/he-she.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/he-she.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package implements a version of semi-automatic pronoun switching for
writing gender-neutral (and possibly annoying) prose. It has upper- and
lowercase versions of switching pronouns for all case forms, plus
anaphoric versions that reflect the current gender choice.

